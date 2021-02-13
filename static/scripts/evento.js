var compartilhar = document.getElementById('whatsapp')

compartilhar.addEventListener('click', function(){
    // coloquei o endereço de forma estatica mas será o do document.domaisn + resto da url
    compartilhar.href = 'https://wa.me/?text=' + compartilhar.href
});