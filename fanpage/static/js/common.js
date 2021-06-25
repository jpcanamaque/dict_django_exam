const delete_post = function (redirect_url) {
    let del_prompt = confirm("Are you sure you want to delete this post? ");
    if(del_prompt) {
        window.location = redirect_url
    }
}