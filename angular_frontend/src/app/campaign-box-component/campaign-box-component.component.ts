import { Component, OnInit,Input } from '@angular/core';
import {CampaignService} from '../campaign.service';
import {Campaign} from '../campaign-model';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-campaign-box-component',
  templateUrl: './campaign-box-component.component.html',
  styleUrls: ['./campaign-box-component.component.css']
})
export class CampaignBoxComponentComponent implements OnInit {
  @Input() campaign_id;
  @Input() campaign_title;
  @Input() campaign_story;
  @Input() campaign_amount;
  @Input() campurl;

  constructor() { }

  ngOnInit() {
  console.log(this.campaign_id)
  }


}
