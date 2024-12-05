// Función para agregar un pedido a Firestore
function agregarPedido() {
    const cliente = document.getElementById("cliente").value;
    const producto = document.getElementById("producto").value;
    const detalle = document.getElementById("detalle").value;
    const fecha_pedido = document.getElementById("fecha_pedido").value;
    const fecha_entrega = document.getElementById("fecha_entrega").value;
    const total = document.getElementById("total").value;

    // Guarda el pedido en Firestore
    db.collection("pedidos").add({
        cliente: cliente,
        producto: producto,
        detalle: detalle,
        fecha_pedido: fecha_pedido,
        fecha_entrega: fecha_entrega,
        total: total
    })
    .then(() => {
        alert("Pedido agregado exitosamente!");
    })
    .catch((error) => {
        console.error("Error agregando el pedido: ", error);
    });
}
