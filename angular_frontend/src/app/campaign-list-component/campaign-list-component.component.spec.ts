import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { CampaignListComponentComponent } from './campaign-list-component.component';

describe('CampaignListComponentComponent', () => {
  let component: CampaignListComponentComponent;
  let fixture: ComponentFixture<CampaignListComponentComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ CampaignListComponentComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(CampaignListComponentComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should be created', () => {
    expect(component).toBeTruthy();
  });
});
