const show = document.querySelector('.password-visibility');
const form = document.querySelector('form');
const password = document.getElementById('id_password');


show.addEventListener('click', () => {
    [password.type, show.firstChild.innerText] = password.type === 'password' ? ['text', 'visibility_off'] : ['password', 'visibility'];
});