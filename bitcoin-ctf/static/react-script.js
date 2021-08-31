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
        if(!currPayerBalance) {
            currPayerBalance = 0;
            localStorage.setItem(id, String(currPayerBalance));
        }

        //payment
        localStorage.setItem(id, String(currPayerBalance-amount));
        this.currBalance = Number(localStorage.getItem(this.id));
        this.currBalance += amount;
        localStorage.setItem(this.id, String(this.currBalance));

        //success code
        return -1;
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
            data: 'blub'
        }
        this.updateState = this.updateState.bind(this)
    };
    updateState(e) {
        this.setState({data: e.target.value});
    }
    render() {
        return (
            <div>
                <h4>BitWallet</h4>
                <form>
                    <input type="text" value={this.state.data} 
                        onChange={this.updateState} />
                </form>
            </div>
        );
    }
}

ReactDOM.hydrate(<Wallet />, document.getElementById("root"));
