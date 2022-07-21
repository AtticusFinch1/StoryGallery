const saveBtn = document.querySelector('.save-changes-btn')
const title = document.querySelector('.title-field')
const descr = document.querySelector('.descr-field')
const author = document.querySelector('.author-field')
const category = document.querySelector('.category-field')
const csrf = document.getElementsByName('csrfmiddlewaretoken')
const postsBox = document.querySelector('#posts-box')
const table_dlt = document.querySelector("#table-delete")
modal = document.querySelector(".modal-content")
const url = "http://127.0.0.1:8000/"

// add post
saveBtn.addEventListener('click', function(e){
    var this_html = $(this) // this=saveBtn=e
    console.log(this_html.parent().parent().children())
    e.preventDefault()
    $.ajax({
        type: 'POST',
        url: url+'add_publication/',
        data: {
            "titleValue" : title.value,
            "descrValue" : descr.value,
            "authorValue" : author.value,
            "categoryValue": category.value,
            "action": 'post',
            'csrfmiddlewaretoken': csrf[0].value,
        },
        success: function(json){
            postsBox.innerHTML += ` <tr id="table-delete" data-id="${json.id}">
                                            <th scope="row">${json.author}</th>
                                            <th class="editable" data-type="title">${json.title}</th>
                                            <th class="editable" data-type="country">${json.description}</th>
                                            <th class="editable" data-type="category">${json.category}</th>
                                            <th class="editable" data-type="username">${json.user}</th>
                                            <td class="btn-td-block"><button type="button" class="btn btn-update" data-toggle="modal" data-id="${json.pk}" data-target="#editModal">
                                                                                                                         <span class="material-icons-sharp">edit</span></button></td>
                                            <td class="btn-td-block"><button class="btn btn-delete" id="${json.id}"><span class="material-icons-sharp">delete</span></button></td>
                                    </tr>`

        },
        error: function(err){
            console.log(err)
        }
    })
    $('#add_post_form')[0].reset();
    setTimeout(() => {
                location.reload()
            }, 2000);

})

// delete post

const del_btns = document.querySelectorAll(".btn-delete")
del_btns.forEach(btn=>{
    btn.addEventListener('click', function(e){
        table_id=$(this)[0].id
        console.log(table_id)
        $.ajax({
            type: 'POST',
            url: url+'delete_publications/',
            data: {
                "id": $(this)[0].id,
                "action": 'post',
                'csrfmiddlewaretoken': csrf[0].value,
            },
            success: function(json){
                $('#table-delete[data-id="' + table_id + '"]').remove();
            },
            error: function(err){
                console.log(err)
            }
        })
    })
})

//edit post
const edit_author = document.querySelector('.author-edit-field')
const edit_title = document.querySelector('.title-edit-field')
const edit_country=document.querySelector('.descr-edit-field')
const edit_cat = document.querySelector('.category-edit-field')
const edit_btns = document.querySelectorAll(".btn-update")
const editModalTitle = document.querySelector('#editModalLabel')
edit_btns.forEach(btn=>{
    btn.addEventListener('click', function(e){
        table_id=$(this)[0].dataset.id
        console.log(edit_author.value)
        $.ajax({
            type: 'POST',
            url: url+'edit_publications/',
            data: {
                "id": table_id,
                "action": 'post',
                'csrfmiddlewaretoken': csrf[0].value,
            },
            success: function(json){
                edit_author.value=json.update_pub.author,
                edit_title.value=json.update_pub.title,
                edit_country.value = json.update_pub.country,
                edit_cat.value=json.update_pub.category
                editModalTitle.innerHTML = json.update_pub.author
            },
            error: function(err){
                console.log(err)
            }
        })
    })
})

//update post

const update_btn = document.querySelector('.edit-changes-btn')
update_btn.addEventListener('click', function(e){
        e.preventDefault()
        $.ajax({
            type: 'POST',
            url: url+'update_publications/',
            data: {
                "action": 'post',
                'csrfmiddlewaretoken': csrf[0].value,
                'editAuthor':edit_author.value,
                'editTitle':edit_title.value,
                'editCountry': edit_country.value,
                'editCategory': edit_cat.value,
                'modalTitle': editModalTitle.innerHTML
            },
            success: function(json){
                edit_author.value=json.data.upd_author,
                edit_title.value=json.data.upd_title,
                edit_country.value = json.data.upd_country,
                edit_cat.value=json.data.upd_cat
            },
            error: function(err){
                console.log(err)
            }
        })
        setTimeout(() => {
                    location.reload()
                }, 2000);
    })

// search
const searchForm = document.getElementById('search-form')
const searchInput = document.getElementById('search-input')
const searchResults = document.getElementById('results-box')

searchInput.addEventListener('keyup', function(e){
    e.preventDefault()
    $.ajax({
        type: 'POST',
        url: url + 'search-publication/',
        data: {
                'csrfmiddlewaretoken': csrf[0].value,
                'action': 'post',
                'data': e.target.value
        },
        success: function(json){
            const data = json.dt
            console.log(data)
            if(Array.isArray(data)){
                searchResults.innerHTML = ''
                data.forEach(function(item){
                    searchResults.innerHTML += `
                        <a href="#" class="item">
                            <div class="search-form__results">
                                <div class="form-results">
                                    <h5>${item.publisher_name}</h5>
                                </div>
                                <div class="form-results">
                                    <h5>${item.publisher_title}</h5>
                                </div>
                                <div class="form-results">
                                    <h5>${item.country}</h5>
                                </div>
                                <div class="form-results">
                                    <h5>${item.cat}</h5>
                                </div>
                            </div>
                        </a>
                    `
                })
                if(searchResults.classList.contains('not-visible')){
                     searchResults.classList.remove('not-visible')
                }
            } else {
                if (searchInput.value.length > 0){
                    searchResults.classList.remove('not-visible')
                    searchResults.innerHTML = `<div class="search-form__results">
                                                    <div class="form-results">
                                                        <h5>${data}</h5>
                                                    </div>
                                                </div>`
                }
                else {
                    searchResults.classList.add('not-visible')
                }
            }
        },
        error: function(err){
            console.log(err)
        }
    })
})



