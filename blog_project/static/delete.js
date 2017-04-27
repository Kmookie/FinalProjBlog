function deletePost(postId) {
    var xhr = new XMLHttpRequest();
    var token = document.cookie.split('=')[1];
    xhr.open("POST", '/post/' + postId, true);
    xhr.setRequestHeader("X-CSRFToken", token);
    xhr.onload = function() {
        location.reload();
    };
    xhr.send(null);
}
