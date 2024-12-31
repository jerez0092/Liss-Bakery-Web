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
    promoContainer.style.flexDirection = 'column';
    promoContainer.style.justifyContent = 'center';
    promoContainer.style.alignItems = 'center';
    promoContainer.style.zIndex = '1000';

    // Crear la imagen promocional
    const promoImage = document.createElement('img');
    promoImage.src = 'catalogo/promos/promo 1.jpeg'; // Reemplaza con la ruta de tu imagen
    promoImage.alt = 'Haz tu pedido para la rosca de rey del 4 al 6 de enero';
    promoImage.style.maxWidth = '50%';
    promoImage.style.maxHeight = '50%';
    promoImage.style.cursor = 'pointer';
    
    // Crear el texto promocional
    const promoText = document.createElement('div');
    promoText.innerHTML = 'Haz tu pedido para la rosca de reyes del 4 al 6 de enero. <a href="https://wa.me/+50363149600" style="color: yellow; text-decoration: underline;">Contáctanos aquí</a>';
    promoText.style.backgroundColor = 'rgba(0, 0, 0, 0.7)';
    promoText.style.color = 'white';
    promoText.style.padding = '10px';
    promoText.style.marginTop = '20px';
    promoText.style.borderRadius = '8px';
    promoText.style.fontSize = '18px';
    promoText.style.textAlign = 'center';

    const promoText2 = document.createElement('div');
    promoText2.innerHTML = 'Toca la imagen para cerrar';
    promoText2.style.backgroundColor = 'rgba(0, 0, 0, 0.7)';
    promoText2.style.color = 'white';
    promoText2.style.padding = '10px';
    promoText2.style.marginTop = '20px';
    promoText2.style.borderRadius = '8px';
    promoText2.style.fontSize = '18px';
    promoText2.style.textAlign = 'center';
    
    // Añadir un evento de clic para cambiar la imagen o eliminar el contenedor
    promoImage.addEventListener('click', () => {
        const filename = promoImage.src.split('/').pop();
        if (filename === 'promo 1.jpeg') {
            promoImage.src = 'promo 2.jpeg'; // Reemplaza con la ruta de la segunda imagen
        } else {
            document.body.removeChild(promoContainer);
        }
    });

    // Añadir la imagen y el texto al contenedor
    promoContainer.appendChild(promoImage);
    promoContainer.appendChild(promoText);
    promoContainer.appendChild(promoText2);

    // Añadir el contenedor al cuerpo del documento
    document.body.appendChild(promoContainer);
});
