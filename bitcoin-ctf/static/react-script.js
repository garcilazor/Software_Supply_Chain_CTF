class Client {
    constructor(id, pubkey) {
        this.id = id
        this.pubkey = pubkey
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
    //static defaultProps = {
    //    id: 'jones',
    //    pubkey: '47DFir0kT32AckW3'
    //}
    updateState(e) {
        this.setState({data: e.target.value});
    }
    render() {
        //var client = new Client(this.props.id, this.props.pubkey);
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

//export default Wallet;

ReactDOM.hydrate(<Wallet />, document.getElementById("root"));
//ReactDOM.hydrate(<Wallet id="jones" pubkey="47DFir0kT32AckW3" />, document.getElementById("root"));
