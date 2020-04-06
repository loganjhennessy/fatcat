import React from 'react';
import StockTable from './StockTable';
import './App.css';

const apiUrl = "http://localhost:8000/api";

function App() {
  return (
    <div className="App">
      <StockTable apiUrl={apiUrl}/>
    </div>
  );
}

export default App;
