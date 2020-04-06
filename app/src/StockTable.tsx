import React from 'react';
import MaterialTable from "material-table";

export interface StockTableProps {
    apiUrl: string
}

type Stock = {
    symbol: string,
    bigFive: boolean,
    stickerPrice: number,
    currentPrice: number
}

type StockTableState = {
    rows: Array<Stock>
};


class StockTable extends React.Component<StockTableProps, StockTableState> {

    constructor(props: StockTableProps) {
        super(props);
        this.state = {
            rows: []
        };
    };

    componentDidMount(): void {
        fetch(this.props.apiUrl)
            .then(res => res.json())
            .then((stocks: Array<Stock>) => {
                this.setState({
                    rows: stocks
                })
            })
            .catch( e => {console.log(e)});
    }

    render() {
        const rows = this.state.rows;
        return (
            <div>
                <MaterialTable
                    columns={[
                        { title: "Symbol", field: "symbol" },
                        { title: "Big Five", field: "bigFive", type: "boolean"},
                        { title: "Sticker Price", field: "stickerPrice", type: "numeric"},
                        { title: "Current Price", field: "currentPrice", type: "numeric"}
                    ]}
                    data={rows}
                    options={{
                        search: true
                    }}
                />
            </div>
        );
    }
}

export default StockTable;
