import { Component, OnInit,Input } from '@angular/core';
import {CampaignService} from '../campaign.service';
import {Campaign} from '../campaign-model';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-campaign-list-component',
  templateUrl: './campaign-list-component.component.html',
  styleUrls: ['./campaign-list-component.component.css']
})
export class CampaignListComponentComponent implements OnInit {



  campaigns: Campaign[];
  private  param;
  @Input() campurl;



  constructor(private campaignslist: CampaignService,private activatedRoute: ActivatedRoute) {
  		let params: any = this.activatedRoute.snapshot.params;		
  		this.param=params.id;		
  		
   }  
   ngOnInit() {
    this.getCampaignByCategory(this.param);
  }  
  
  getCampaignByCategory(id): void {
    this.campaignslist.getCampaignByCategory(id)
          .subscribe(campaigns => {
           this.campaigns = campaigns;
           console.log('data',campaigns);
        });
  }

}
