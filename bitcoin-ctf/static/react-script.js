class Client {
    constructor(id, pubkey) {
        this.id = id
        this.pubkey = pubkey
        this.currBalance = Number(localStorage.getItem(id));
        if (!this.currBalance) {
            localStorage.setItem(id, '1200')
        }
    };

    payment(id, pubkey, amount) {
        /* Placeholder: some cryptography code using both pubkey's */

        //check balances
        var currPayerBalance = Number(localStorage.getItem(id));
        this.currBalance = Number(localStorage.getItem(this.id));
        if(!currPayerBalance) {
            currPayerBalance = 10;
            localStorage.setItem(id, String(currPayerBalance));
        }
        if((currPayerBalance < amount && amount > 0) || (this.currBalance < (amount*-1) && amount < 0)) {
            console.log("Insufficient funds")
            return false;
        }

        //payment
        localStorage.setItem(id, String(currPayerBalance-amount));
        this.currBalance += amount;
        localStorage.setItem(this.id, String(this.currBalance));

        //success code
        return true;
    }

    withdrawal(amount, id, pubkey) {
        /* Placeholder: some cryptography code using both pubkey's */
        return this.payment(id, pubkey, amount * -1);
    }

    getBalance() {
        return this.currBalance;
    }
}

class Wallet extends React.Component {
    constructor(props) {
        super(props);
        this.props.id = 'jones';
        this.props.pubkey = '47DFir0kT32AckW3';

        this.client=new Client(this.props.id, this.props.pubkey)
        this.state={
            id: "",
            key: "",
            coins: 0
        }
        this.updateState = this.updateState.bind(this)
        this.transaction = this.transaction.bind(this)
    };
    updateState(e) {
        const key = e.target.name;
        const value = e.target.value;
        this.setState({ [key]: value });
    }
    transaction(e) {
        var success = this.client.payment(this.state.id, this.state.key, this.state.coins)
        console.log("transaction complete")
        if (success) {
            document.getElementById("success-message").innerHTML = "Successfull payment!"
        } else {
            document.getElementById("success-message").innerHTML = "Payment denied!"
        }
    }
    render() {
        return (
            <div>
                <h4>Donate to us with BitWallet!</h4>
                <h3>BitWallet ID:</h3>
                <input name="id" type="text" value={this.state.id} 
                    onChange={this.updateState} />
                <h3>BitWallet Public Key:</h3>
                <input name="key" type="text" value={this.state.key}
                    onChange={this.updateState} />
                <h3>Payment Amount:</h3>
                <input name="coins" type="number" value={this.state.coins}
                    onChange={this.updateState} />
                <br />
                <button onClick={this.transaction} title="pay">
                    Donate!
                </button>
                <p id="success-message"></p>
            </div>
        );
    }
}

ReactDOM.hydrate(<Wallet />, document.getElementById("root"));
