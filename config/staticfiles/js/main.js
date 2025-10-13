const date = new Date();
document.querySelector(".year").innerHTML = date.getFullYear();

setTimeout(() => {
    $("#message").fadeOut("slow");   //find message id and diabled it, jquery fadeout method
}, 3000);

