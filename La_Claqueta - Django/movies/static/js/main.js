/* FOOTER ---------------------------------- */

function suscribeFunction() {
    let userEmail = document.getElementById('useremail');
    console.log(userEmail.value);
    let validEmail =  /^\w+([.-_+]?\w+)*@\w+([.-]?\w+)*(\.\w{2,10})+$/;
    const swalMessage = Swal.mixin({
        customClass: {
          title: 'swalTitle',
        },
        buttonsStyling: false
      })
    if (validEmail.test(userEmail.value) ){
        /* console.log("La dirección de email " + user.value + " es correcta."); */
        swalMessage.fire({
            title: 'Te has inscripto en el newsletter correctamente con el correo ' + userEmail.value,
            showConfirmButton: false,
            timer: 4000,
        })
    } else {
        /* console.log("La dirección de email es incorrecta."); */
        swalMessage.fire({
            title: 'El correo ingresado es incorrecto. Por favor intentelo de nuevo.',
            showConfirmButton: false,
            timer: 4000,
        })
    };
    document.getElementById('useremail').reset();
}