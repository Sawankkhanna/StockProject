import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Category } from 'src/app/models/category';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-category',
  templateUrl: './category.component.html',
  styleUrls: ['./category.component.css']
})
export class CategoryComponent implements OnInit {
  categories!: Category[];
  constructor(private http: HttpClient) {}

  ngOnInit() {
    this.http.get<Category[]>('http://localhost:8000/api/categories').subscribe(
      (data) => {
        this.categories = data;
      },
      (error) => {
        console.error('Error fetching categories: ', error);
      }
    );
  }
}
