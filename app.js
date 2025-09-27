
(function(){
  const tg = window.Telegram?.WebApp;
  if (!tg) {
    alert('Telegram WebApp SDK topilmadi. Sahifani Telegram ichida oching.');
    return;
  }

  tg.expand(); // maksimal balandlik
  const userBox = document.getElementById('user');
  const status = document.getElementById('status');

  const u = tg.initDataUnsafe?.user;
  userBox.textContent = u ? `@${u.username || 'no_username'} · id: ${u.id}` : 'Foydalanuvchi maʼlumotlari yoʻq';

  function send(action) {
    const payload = { action, ts: Date.now() };
    status.textContent = 'Yuborilyapti…';
    try {
      tg.sendData(JSON.stringify(payload)); // Botga service message sifatida boradi va app yopiladi
    } catch (e) {
      status.textContent = 'Xato: ' + e.message;
    }
  }

  document.getElementById('tapBtn').addEventListener('click', () => send('tap'));
  document.getElementById('dailyBtn').addEventListener('click', () => send('daily'));
  document.getElementById('statsBtn').addEventListener('click', () => send('stats'));
})();
