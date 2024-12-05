// Función para buscar pedidos por fecha de entrega
function buscarPedidos() {
    const fechaEntrega = document.getElementById("fecha_entrega").value;
    const pedidosDiv = document.getElementById("pedidos");
    pedidosDiv.innerHTML = ''; // Limpiar el contenido previo

    db.collection("pedidos")
        .where("fecha_entrega", "==", fechaEntrega)
        .get()
        .then((querySnapshot) => {
            if (querySnapshot.empty) {
                pedidosDiv.innerHTML = '<p>No hay pedidos para la fecha seleccionada.</p>';
                return;
            }

            querySnapshot.forEach((doc) => {
                const pedido = doc.data();
                const pedidoDiv = document.createElement("div");
                pedidoDiv.className = "pedido";
                pedidoDiv.innerHTML = `
                    <p><strong>Cliente:</strong> ${pedido.cliente}</p>
                    <p><strong>Producto:</strong> ${pedido.producto}</p>
                    <p><strong>Detalle:</strong> ${pedido.detalle}</p>
                    <p><strong>Fecha Pedido:</strong> ${pedido.fecha_pedido}</p>
                    <p><strong>Fecha Entrega:</strong> ${pedido.fecha_entrega}</p>
                    <p><strong>Total:</strong> $${pedido.total}</p>
                `;
                pedidosDiv.appendChild(pedidoDiv);
            });
        })
        .catch((error) => {
            console.error("Error obteniendo los pedidos: ", error);
        });
}
