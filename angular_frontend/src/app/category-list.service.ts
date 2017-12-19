import { ReturnStatement } from '@angular/compiler/compiler';
import { Injectable } from '@angular/core';
import {Category} from './category';
import { Observable } from 'rxjs/Observable';
import { of } from 'rxjs/observable/of';
import { Http } from '@angular/http';
import 'rxjs/add/operator/map'
import { environment } from '../environments/environment';


@Injectable()
export class CategoryListService {

 constructor(private http: Http) { }

getCategories():Observable<Category[]> {
        return this.http.get(environment.apiendpoint+'categories/')
      .map(response =>  <Category[]>response.json());
  }


}




