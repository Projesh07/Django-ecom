import { Component,OnInit } from '@angular/core';
import {CategoryBoxComponent} from '../categorybox/categorybox.component';
import {CategoryListService} from '../category-list.service';
import {Category} from '../category';
@Component({
    selector:'category',
    templateUrl:'./category.component.html',
    styleUrls:['./category.component.css'],
})

export class CategoryComponent implements OnInit{
  categories: Category[];
  constructor(private categoryListService: CategoryListService) { }  
  ngOnInit() {
    this.getCategories();
  }  
  getCategories(): void {
    this.categoryListService.getCategories()
        .subscribe(categories => this.categories = categories);
  }
}