import { Component, OnInit } from '@angular/core';
import {CategoryListService} from '../category-list.service';
import {Category} from '../category';
@Component({
  selector: 'app-category-small-list-component',
  templateUrl: './category-small-list-component.component.html',
  styleUrls: ['./category-small-list-component.component.css']
})
export class CategorySmallListComponentComponent implements OnInit {

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
