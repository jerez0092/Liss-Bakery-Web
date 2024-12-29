document.addEventListener('DOMContentLoaded', () => {
    // Crear el contenedor de la imagen promocional
    const promoContainer = document.createElement('div');
    promoContainer.style.position = 'fixed';
    promoContainer.style.top = '0';
    promoContainer.style.left = '0';
    promoContainer.style.width = '100%';
    promoContainer.style.height = '100%';
    promoContainer.style.backgroundColor = 'rgba(0, 0, 0, 0.5)';
    promoContainer.style.display = 'flex';
    promoContainer.style.justifyContent = 'center';
    promoContainer.style.alignItems = 'center';
    promoContainer.style.zIndex = '1000';

    // Crear la imagen promocional
    const promoImage = document.createElement('img');
    promoImage.src = 'catalogo/promos/promo 1.jpeg'; // Reemplaza con la ruta de tu imagen
    promoImage.alt = 'Haz tu pedido para la rosca de rey del primero de enero al 4 de enero';
    promoImage.style.maxWidth = '90%';
    promoImage.style.maxHeight = '90%';
    promoImage.style.cursor = 'pointer';
    
    // Añadir un evento de clic para cambiar la imagen o eliminar el contenedor
    promoImage.addEventListener('click', () => {
        if (promoImage.src.includes('catalogo/promos/promo 2.jpeg')) {
            promoImage.src = 'tu-imagen-promocional2.png'; // Reemplaza con la ruta de la segunda imagen
        } else {
            document.body.removeChild(promoContainer);
        }
    });

    // Añadir la imagen al contenedor
    promoContainer.appendChild(promoImage);

    // Añadir el contenedor al cuerpo del documento
    document.body.appendChild(promoContainer);
});
