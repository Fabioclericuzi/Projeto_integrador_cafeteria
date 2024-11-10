let cart = []
let isUserValidated = false

async function validateUser() {
    const cpf = document.getElementById('cpf').value.trim();

    if (cpf === '') {
        alert('Por favor, insira seu CPF.');
        return;
    }

    const response = await fetch(`/validate-user?cpf=${cpf}`);
    const result = await response.json();

    console.log(result);

    if (result.valid) {
        isUserValidated = true;
        document.getElementById('menu-section').style.display = 'block';

        const validationMessage = document.getElementById('validation-message');
        validationMessage.textContent = 'Usuário validado com sucesso!';
        validationMessage.classList.remove('d-none');
    } else {
        const redirect = confirm('CPF não encontrado. Deseja se cadastrar?');
        if (redirect) {
            window.location.href = '/cadastro';
        } else {
            window.location.href = '/';
        }
    }
}

function addToCart(name, price) {
    if (!isUserValidated) {
        alert('Você precisa validar seu CPF antes de fazer um pedido.')
        return
    }
    cart.push({ name, price, quantity: 1 })
    updateCart()
}

function removeFromCart(index) {
    cart.splice(index, 1)
    updateCart()
}

function clearCart() {
    cart = []
    updateCart()
}

async function finalizePurchase() {
    console.log("Carrinho:", cart);
    if (cart.length === 0) {
        alert('Seu carrinho está vazio.')
        return
    }

    if (!isUserValidated) {
        alert('Você precisa validar seu CPF antes de fazer um pedido.')
        return
    }

    const cpf = document.getElementById('cpf').value.trim()

    for (const item of cart) {
        if (!item.name || item.price == null || item.quantity == null || item.quantity <= 0) {
            alert(`O item ${item.name || 'desconhecido'} tem uma quantidade inválida.`)
            return
        }
    }

    const total = cart.reduce((sum, item) => sum + (item.price * item.quantity), 0)

    const response = await fetch('/finalize-order/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            cpf: cpf,
            items: cart.map(item => ({
                name: item.name,
                price: item.price,
                quantity: item.quantity  // A quantidade de cada item
            })),
            total: total
        })
    })

    const result = await response.json()

    if (result.success) {
        const purchaseMessage = document.getElementById('purchase-message')
        purchaseMessage.textContent = `Pedido realizado com sucesso! Total: R$ ${result.total.toFixed(2)}. Itens: ${result.items.map(item => item.nome_produto).join(', ')}`
        purchaseMessage.classList.remove('d-none')

        clearCart()
    } else {
        alert(`Erro: ${result.message}`)
    }
}

function updateCart() {
    const cartItemsContainer = document.getElementById('cart-items');
    const cartTotalContainer = document.getElementById('cart-total');
    cartItemsContainer.innerHTML = '';
    let total = 0;

    cart.forEach((item, index) => {
        const itemDiv = document.createElement('div');
        itemDiv.classList.add('cart-item');
        itemDiv.innerHTML = `
            <span>${item.name}</span>
            <span>R$ ${item.price.toFixed(2)}</span>
            <span>Quantidade: <input type="number" value="${item.quantity}" onchange="updateQuantity(${index}, this.value)" /></span>
            <button class="remove-button" onclick="removeFromCart(${index})">❌</button>
        `;
        cartItemsContainer.appendChild(itemDiv);
        total += item.price * item.quantity;
    });

    cartTotalContainer.textContent = `Total: R$ ${total.toFixed(2)}`;
}

function updateQuantity(index, quantity) {
    if (quantity <= 0) {
        alert('Quantidade deve ser maior que zero');
        return;
    }
    cart[index].quantity = quantity;
    updateCart();
}
