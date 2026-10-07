/* Appellation Winery of the Month: shared page behavior. */

/* ---------- tabs ---------- */
function showTab(name) {
  document.querySelectorAll(".tab-panel").forEach(function (p) { p.classList.toggle("active", p.id === "tab-" + name); });
  document.querySelectorAll(".tab-btn").forEach(function (b) { b.classList.toggle("active", b.dataset.tab === name); });
}
document.querySelectorAll(".tab-btn").forEach(function (b) {
  b.addEventListener("click", function () { showTab(b.dataset.tab); });
});

/* ---------- copy link buttons ---------- */
document.querySelectorAll(".copy-btn").forEach(function (b) {
  b.addEventListener("click", function (e) {
    e.preventDefault();
    var url = new URL(b.dataset.href, window.location.href).href;
    navigator.clipboard.writeText(url).then(function () {
      var t = b.textContent;
      b.textContent = "Copied";
      setTimeout(function () { b.textContent = t; }, 1600);
    });
  });
});

/* ---------- contact gate ----------
   Winery contact names, emails and phone numbers are NOT in this site's files.
   They live in Supabase (public.winery_contacts) and are readable only by
   emails marked active in public.viewer_allowlist, enforced by RLS.
   The key below is a publishable key. Never put a service_role key here. */
(function () {
  var bar = document.getElementById("authbar");
  if (!bar || !window.supabase) return;

  var SUPABASE_URL = "https://vkxjggeuicfrmenqdskl.supabase.co";
  var SUPABASE_KEY = "sb_publishable_hNfH9nVJ2r60imC6MeMhOA_DaA1NtWk";
  var db = window.supabase.createClient(SUPABASE_URL, SUPABASE_KEY);
  var $ = function (id) { return document.getElementById(id); };
  var esc = function (s) {
    return String(s == null ? "" : s).replace(/[&<>"']/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
    });
  };
  var emailOk = function (e) { return /^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(e); };
  var SESSION = null;

  function msg(text, isErr) {
    var m = $("ab-msg");
    m.className = "ab-msg" + (isErr ? " err" : "");
    m.textContent = text || "";
  }

  $("ab-signin").addEventListener("click", async function () {
    var email = $("ab-email").value.trim().toLowerCase();
    var password = $("ab-pass").value;
    if (!emailOk(email) || !password) { msg("Enter your email and password.", true); return; }
    msg("Signing in…");
    var r = await db.auth.signInWithPassword({ email: email, password: password });
    if (r.error) msg(r.error.message, true);
  });
  $("ab-link").addEventListener("click", async function () {
    var email = $("ab-email").value.trim().toLowerCase();
    if (!emailOk(email)) { msg("Enter a valid email address.", true); return; }
    msg("Sending…");
    var r = await db.auth.signInWithOtp({ email: email, options: { emailRedirectTo: window.location.href.split("#")[0] } });
    if (r.error) msg(r.error.message, true);
    else msg("Check your inbox. The link opens this schedule.");
  });
  ["ab-email", "ab-pass"].forEach(function (id) {
    $(id).addEventListener("keydown", function (e) { if (e.key === "Enter") $("ab-signin").click(); });
  });
  $("ab-signout").addEventListener("click", async function () { await db.auth.signOut(); location.reload(); });

  function showSignedIn() {
    $("ab-note").textContent = "Signed in as " + (SESSION.user.email || "") + ".";
    ["ab-email", "ab-pass", "ab-signin", "ab-link"].forEach(function (id) { $(id).classList.add("hidden"); });
    $("ab-signout").classList.remove("hidden");
  }

  async function reveal() {
    var r = await db.from("winery_contacts").select("*");
    showSignedIn();
    if (r.error || !r.data || !r.data.length) {
      msg((SESSION.user.email || "You") + " is signed in, but this account is not approved to view contacts.", true);
      return;
    }
    var bySlug = {};
    r.data.forEach(function (row) { bySlug[row.slug] = row; });
    var shown = 0, missing = 0;
    document.querySelectorAll(".wd-contact").forEach(function (el) {
      var row = bySlug[el.getAttribute("data-w")];
      if (!row) { missing++; el.innerHTML = '<span class="wd-key">Contact</span><span class="tbd-text">Not on file yet</span>'; return; }
      var bits = [];
      if (row.contact_name) bits.push(esc(row.contact_name));
      if (row.contact_email) bits.push('<a href="mailto:' + esc(row.contact_email) + '">' + esc(row.contact_email) + "</a>");
      if (row.contact_phone) bits.push(esc(row.contact_phone));
      el.innerHTML = '<span class="wd-key">Contact</span>' + (bits.join(" &middot; ") || '<span class="tbd-text">Not on file yet</span>');
      shown++;
    });
    $("ab-note").textContent = "Signed in as " + (SESSION.user.email || "") + ". Contact details are visible below" +
      (missing ? " (" + missing + " not on file yet)." : ".");
    msg("");
  }

  (async function boot() {
    var s = (await db.auth.getSession()).data.session;
    db.auth.onAuthStateChange(function (_e, sess) { if (sess && !SESSION) { SESSION = sess; reveal(); } });
    if (s && !SESSION) { SESSION = s; reveal(); }
  })();
})();
