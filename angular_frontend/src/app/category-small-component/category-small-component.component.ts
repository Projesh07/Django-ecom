// import { Input } from '@angular/core/core';
import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-category-small-component',
  templateUrl: './category-small-component.component.html',
  styleUrls: ['./category-small-component.component.css']
})
export class CategorySmallComponentComponent {
@Input () name;
@Input () image;
@Input () url;

  constructor() { }

  ngOnInit() {
  }

}
