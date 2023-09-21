import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { StocksService } from 'src/app/services/stocks.service';
import { Stock } from 'src/app/models/stock';

@Component({
  selector: 'app-stock',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './stock.component.html',
  styleUrls: ['./stock.component.css']
})
export class StockComponent implements OnInit{

  stockList!: Stock[];
  constructor(private _stocksService: StocksService) {}
  
  ngOnInit(): void {
    this._stocksService.getStocks().subscribe((data) => {
      this.stockList = data;
      console.log('Data: ' + this.stockList);
    })
  }

  showStocks(): void {
    this._stocksService.getStocks().subscribe((data) => {
      this.stockList = data;
    })
  }

  getInfo(symbol: string) {
    // TODO
  }

  addWatchlist(symbol: string) {
    // TODO
  }

}
