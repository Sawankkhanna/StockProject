import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { STOCKLIST } from '../components/stock/stocklist';
import { Stock } from '../models/stock';

@Injectable({
  providedIn: 'root'
})
export class StocksService {

  private url: string = 'http://localhost:8000/api/stocks/';

  constructor(private http: HttpClient) {}

  httpOptions = {
    headers: new HttpHeaders({
      'Content-Type': 'application/json'
    })
  };

  getStocks(): Observable<Stock[]> {
    return this.http.get<Stock[]>(
      this.url
    );
  }
}
