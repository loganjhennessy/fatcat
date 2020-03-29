import React from 'react';
import './App.css';

type StockTableState = {
    rows: JSX.Element[]
};
class StockTable extends React.Component<{}, StockTableState> {

    constructor(props: object) {
        super(props);
        this.state = {
            rows: []
        };
    };

    componentDidMount(): void {
        const stocks = [
            {
                symbol: "DAL",
                bigFive: true,
                stickerPrice: 45.00,
                currentPrice: 29.00
            }
        ];
        this.setState({
            rows: stocks.map((stock) =>
                <tr>
                    <td>{stock.symbol}</td>
                    <td>{String(stock.bigFive)}</td>
                    <td>{stock.stickerPrice}</td>
                    <td>{stock.currentPrice}</td>
                </tr>
            )
        });
    }

    render() {
        const rows = this.state.rows;
        return (
            <div>
                <table>
                    <tr>
                        <th>Symbol</th>
                        <th>Big Five</th>
                        <th>Sticker Price</th>
                        <th>Current Price</th>
                    </tr>
                    {rows}
                </table>
            </div>
        );
    }
}

export default StockTable;
