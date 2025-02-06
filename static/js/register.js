const form = document.querySelector('form');
const username = document.getElementById('id_username');
const [pass1, pass2] = document.querySelectorAll('.password-input');
const [vis1, vis2] = document.querySelectorAll('.password-visibility');
const [warn1, warn2, warn3,,, warn4] = document.querySelectorAll('.warn');

function validatePassword(password, personalInfo) {
    console.log(pass1);
    
    if (password.length < 8) {
        return false;
    }

    if (/^\d+$/.test(password)) {
        return false;
    }

    if (password.toLowerCase().includes(personalInfo.toLowerCase())) {
        return false;
    }

    return true;
}

vis1.addEventListener('click', () => {
    [pass1.type, vis1.firstChild.innerText] = pass1.type === 'password' ? ['text', 'visibility_off'] : ['password', 'visibility'];
});

vis2.addEventListener('click', () => {
    [pass2.type, vis2.firstChild.innerText] = pass2.type === 'password' ? ['text', 'visibility_off'] : ['password', 'visibility'];
});

form.addEventListener('submit', event => {
    event.preventDefault();

    [warn1, warn2, warn3, warn4].forEach(warn => warn.classList.add('hidden'));

    if (pass1.value !== pass2.value) {
        warn4.classList.remove('hidden');
        return
    }
    if (!validatePassword(pass1.value, username.value)) {

    }
    pass1.type = 'password';
    pass2.type = 'password';
    form.submit();
});
