import { CategoryBoxComponent } from './categorybox/categorybox.component';
import { FooterComponent } from './footer/footer.component';
import { NavbarComponent } from './navbar/navbar.component';
import { CategoryComponent } from './category/category.component';
import { SliderComponent } from './slider/slider.component';
import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { AppComponent } from './app.component';
import { HomeComponentComponent } from './home-component/home-component.component';
import { CampaignComponentComponent } from './campaign-component/campaign-component.component';
import { CampaignBoxComponentComponent } from './campaign-box-component/campaign-box-component.component';
import { CampaignListComponentComponent } from './campaign-list-component/campaign-list-component.component';
import { CampaignHeadingComponentComponent } from './campaign-heading-component/campaign-heading-component.component';
import { CategorySmallComponentComponent } from './category-small-component/category-small-component.component';
import { CategorySmallListComponentComponent } from './category-small-list-component/category-small-list-component.component';

import {routing} from './app.routing';
import { TopDonationComponent } from './top-donation/top-donation.component';
import { TopDonationListComponent } from './top-donation-list/top-donation-list.component';
import { RecentDonationListComponent } from './recent-donation-list/recent-donation-list.component';
import { RecentDonationComponent } from './recent-donation/recent-donation.component';
import { CampDetailsComponent } from './camp-details/camp-details.component';
import { DonationListComponent } from './donation-list/donation-list.component';
import { CampaingnPageComponent } from './campaingn-page/campaingn-page.component';
import {CategoryListService} from './category-list.service';
import {CampaignService} from './campaign.service';
import { HttpModule, RequestOptions } from '@angular/http';
import { MaterializeModule } from "angular2-materialize";

import {TimeAgoPipe} from 'time-ago-pipe'

@NgModule({
  declarations: [
    AppComponent,
    NavbarComponent,
    SliderComponent,
    CategoryComponent,
    FooterComponent,
    CategoryBoxComponent,
    HomeComponentComponent,
    CampaignComponentComponent,
    CampaignBoxComponentComponent,
    CampaignListComponentComponent,
    CampaignHeadingComponentComponent,
    CategorySmallComponentComponent,
    CategorySmallListComponentComponent,
    TopDonationComponent,
    TopDonationListComponent,
    RecentDonationListComponent,
    RecentDonationComponent,
    CampDetailsComponent,
    DonationListComponent,
    CampaingnPageComponent,
    TimeAgoPipe,
  ],
  imports: [
    BrowserModule,routing,HttpModule,MaterializeModule
  ],
  providers: [CategoryListService,CampaignService],
  bootstrap: [AppComponent]
})
export class AppModule { }
