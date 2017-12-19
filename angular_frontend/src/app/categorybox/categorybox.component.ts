import { Component,Input } from '@angular/core';
@Component({
    selector:"categorybox",
    templateUrl:"./categorybox.component.html",
    styleUrls:["./categorybox.component.css"],
})

export class CategoryBoxComponent{
    @Input() name;
    @Input() description;
    @Input() image;
    @Input() url;
    @Input() cid;
}