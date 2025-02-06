const textarea = document.querySelector("textarea");
const ratings = document.querySelectorAll('.rating');
const rating = document.getElementById('id_rating');
const ratingsContainer = document.getElementById('rating');

function adjustHeight(textarea) {
    textarea.style.height = "10px";
    textarea.style.height = textarea.scrollHeight + "px";
}

adjustHeight(textarea);

textarea.addEventListener("input", () => {
    adjustHeight(textarea);
});

function star(val1, val2) {
    return  val1 <= val2 ? '★' : '☆'
}

ratings.forEach(e => {
    e.addEventListener('click', () => {
        let rate = parseInt(e.getAttribute('data-val'));
        
        rating.value = rate;
        for (let el of ratings) {
            el.innerText = star(parseInt(el.getAttribute('data-val')), rate);
        }
    });
});
