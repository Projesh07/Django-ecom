import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { CampDetailsComponent } from './camp-details.component';

describe('CampDetailsComponent', () => {
  let component: CampDetailsComponent;
  let fixture: ComponentFixture<CampDetailsComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ CampDetailsComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(CampDetailsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should be created', () => {
    expect(component).toBeTruthy();
  });
});
