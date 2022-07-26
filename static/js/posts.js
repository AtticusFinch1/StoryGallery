const parallax = document.getElementById('parallax')
const parallax_text = document.getElementById('parallax-text')
window.addEventListener("scroll", function(){
    let offset = window.pageYOffset; // gets the page Y offset coordinates
//    console.log("Offset:" + offset);
    parallax.style.backgroundPositionY = offset * 0.05 + "px";
})

const one = document.getElementById('first');
const two  = document.getElementById('second');
const three = document.getElementById('third');
const four = document.getElementById('forth');
const five = document.getElementById('fifth');

const form = document.querySelector('.rate-form')
const confirmBox = document.getElementById('confirm-box')
const csrf = document.getElementsByName('csrfmiddlewaretoken')

const handelStarSelect = function(size){
    const children = form.children
    for(let i = 0; i < children.length; i++){
        if(i <= size) {
            children[i].classList.add('checked')
        } else {
            children[i].classList.remove('checked')
        }
    }
}

const handleSelect = function(selection){
    switch(selection){
        case 'first': {
//            one.classList.add('checked')
//            two.classList.remove('checked')
//            three.classList.remove('checked')
//            four.classList.remove('checked')
//            five.classList.remove('checked')
            handelStarSelect(1)
            return
        }
        case 'second': {
            handelStarSelect(2)
            return
        }
        case 'third': {

            handelStarSelect(3)
            return
        }
        case 'forth': {

            handelStarSelect(4)
            return
        }
        case 'fifth': {
            handelStarSelect(5)
            return
        }
    }
}

const getNumericValue = (stringValue) => {
    let numericValue;
    if (stringValue === 'first'){
        numericValue = 1
    }
    else if (stringValue === 'second'){
        numericValue = 2
    }
    else if (stringValue === 'third'){
        numericValue = 3
    }
    else if (stringValue === 'forth'){
        numericValue = 4
    }
    else if (stringValue === 'fifth'){
        numericValue = 5
    }
    return numericValue
}

if (one) {
    const arr = [one, two, three, four, five];

    arr.forEach(item => item.addEventListener('mouseover', (event) => {
    handleSelect(event.target.id);
    }))

    arr.forEach(item => item.addEventListener('click', (event) => {
        const val = event.target.id // id of clicked star

        let isSubmit = false
        form.addEventListener('submit', e => {
            e.preventDefault();
            if (isSubmit){ // to avoid multiple ajax calls to be able to rate multiple times
                return
            }
            isSubmit = true
            const id = e.target.id; // id of post form
            const val_num = getNumericValue(val);
            $.ajax({
                type: 'POST',
                url: '/rate-post/',
                data: {
                    'csrfmiddlewaretoken':csrf[0].value,
                    'el_id' : id,
                    'val': val_num,
                },
                success: function(response){
                    console.log(response)
                    setTimeout(()=>{
                        confirmBox.innerHTML = `<h1>Thank you for rating this article. Your rate is ${response.score}`
                        form.style.display="none"
                    },500)

                    form.style.display = "none"
                },
                error: function(error){
                    console.log(error)
                    confirmBox.innerHTML = `<h1>Something went wrong</h1>`

                }
            })
        })
    }))
}

// --------xx-------- popup functionality -----------xx------//

parallax.addEventListener('click', function(e){
    popup.style.display = "none";
    })