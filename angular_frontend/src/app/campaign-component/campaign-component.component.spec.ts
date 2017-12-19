import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { CampaignComponentComponent } from './campaign-component.component';

describe('CampaignComponentComponent', () => {
  let component: CampaignComponentComponent;
  let fixture: ComponentFixture<CampaignComponentComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ CampaignComponentComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(CampaignComponentComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should be created', () => {
    expect(component).toBeTruthy();
  });
});
