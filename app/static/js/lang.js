const tg = window.Telegram.WebApp;
const lang = tg.initDataUnsafe?.user?.language_code || 'en';

const urlParams = new URLSearchParams(window.location.search);
const currentLang = urlParams.get('lang');

if (!currentLang) {
    // Gắn ?lang=... vào URL hiện tại
    urlParams.set('lang', lang);
    window.location.search = urlParams.toString();
}
