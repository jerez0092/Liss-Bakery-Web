function agregarPedido() {
    const cliente = document.getElementById('cliente').value;
    const producto = document.getElementById('producto').value;
    const detalle = document.getElementById('detalle').value;
    const fecha_pedido = document.getElementById('fecha_pedido').value;
    const fecha_entrega = document.getElementById('fecha_entrega').value;
    const total = document.getElementById('total').value;

    fetch('http://127.0.0.1:5500/add_pedido', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ cliente, producto, detalle, fecha_pedido, fecha_entrega, total })
    })
    .then(response => response.json())
    .then(data => {
        alert('Pedido agregado exitosamente');
        obtenerPedidos();
    })
    .catch(error => console.error('Error:', error));
}

function obtenerPedidos() {
    fetch('http://127.0.0.1:5500/pedidos')
    .then(response => response.json())
    .then(data => {
        const pedidosDiv = document.getElementById('pedidos');
        pedidosDiv.innerHTML = data.map(pedido => `
            <div>
                <strong>Cliente:</strong> ${pedido.cliente} <br>
                <strong>Producto:</strong> ${pedido.producto} <br>
                <strong>Detalle:</strong> ${pedido.detalle} <br>
                <strong>Fecha de Pedido:</strong> ${pedido.fecha_pedido} <br>
                <strong>Fecha de Entrega:</strong> ${pedido.fecha_entrega} <br>
                <strong>Total:</strong> ${pedido.total}
            </div>
            <hr>
        `).join('');
    })
    .catch(error => console.error('Error:', error));
}

document.addEventListener('DOMContentLoaded', obtenerPedidos);
