const { JSDOM } = require('jsdom');

let cart = [];
let isUserValidated = false;

const dom = new JSDOM(`
    <div>
        <input id="cpf" value="12345678909" />
        <div id="menu-section" style="display: none;"></div>
        <div id="validation-message" class="d-none"></div>
        <div id="cart-items"></div>
        <div id="cart-total"></div>
        <div id="purchase-message"></div>
    </div>
`);
global.document = dom.window.document;
global.window = dom.window;

async function validateUser() {
    const cpf = document.getElementById('cpf').value;
    if (!cpf) {
        window.alert('Por favor, insira seu CPF.');
        return;
    }

    const response = { valid: cpf === '12345678909' };
    if (response.valid) {
        isUserValidated = true;
        document.getElementById('menu-section').style.display = 'block';
        document.getElementById('validation-message').textContent = 'Usuário validado com sucesso!';
    } else {
        window.location.href = '/cadastro';
    }
}

function addToCart(name, price) {
    if (!isUserValidated) {
        window.alert('Você precisa validar seu CPF antes de fazer um pedido.');
        return;
    }
    const item = cart.find((item) => item.name === name);
    if (item) {
        item.quantity++;
    } else {
        cart.push({ name, price, quantity: 1 });
    }
}

async function finalizePurchase() {
    if (cart.length === 0) {
        window.alert('Seu carrinho está vazio.');
        return;
    }
    const response = { success: true, total: 10.0 };
    if (response.success) {
        cart = [];
        document.getElementById('purchase-message').textContent = 'Pedido realizado com sucesso!';
    }
}

beforeEach(() => {
    cart = [];
    isUserValidated = false;
});

describe('validateUser', () => {
    it('should alert when CPF is empty', async () => {
        document.getElementById('cpf').value = '';
        const alertMock = jest.spyOn(window, 'alert').mockImplementation(() => {});

        await validateUser();

        expect(alertMock).toHaveBeenCalledWith('Por favor, insira seu CPF.');
        alertMock.mockRestore();
    });

    it('should validate user successfully', async () => {
        document.getElementById('cpf').value = '12345678909';

        await validateUser();

        expect(isUserValidated).toBe(true);
        expect(document.getElementById('menu-section').style.display).toBe('block');
        expect(document.getElementById('validation-message').textContent).toBe('Usuário validado com sucesso!');
    });

});

describe('addToCart', () => {
    it('should add an item to the cart if user is validated', () => {
        isUserValidated = true;
        addToCart('Café', 5.0);

        expect(cart).toHaveLength(1);
        expect(cart[0]).toEqual({ name: 'Café', price: 5.0, quantity: 1 });
    });

    it('should not add to cart if user is not validated', () => {
        const alertMock = jest.spyOn(window, 'alert').mockImplementation(() => {});
        addToCart('Café', 5.0);

        expect(cart).toHaveLength(0);
        expect(alertMock).toHaveBeenCalledWith('Você precisa validar seu CPF antes de fazer um pedido.');
        alertMock.mockRestore();
    });
});

describe('finalizePurchase', () => {
    it('should not finalize purchase if cart is empty', async () => {
        const alertMock = jest.spyOn(window, 'alert').mockImplementation(() => {});

        await finalizePurchase();

        expect(alertMock).toHaveBeenCalledWith('Seu carrinho está vazio.');
        alertMock.mockRestore();
    });

    it('should finalize purchase successfully', async () => {
        isUserValidated = true;
        cart.push({ name: 'Café', price: 5.0, quantity: 2 });

        await finalizePurchase();

        expect(cart).toHaveLength(0);
        expect(document.getElementById('purchase-message').textContent).toBe('Pedido realizado com sucesso!');
    });
});
