import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ServicesComponent } from './components/services/services.component';
import { ProjectsComponent } from './components/projects/projects.component';
import { BrandsComponent } from './components/brands/brands.component';
import { ClientsComponent } from './components/clients/clients.component';
import { AboutComponent } from './components/about/about.component';
import { SolutionsComponent } from './components/solutions/solutions.component';
import { DesignToolComponent } from './components/design-tool/design-tool.component';
import { CaseStudiesComponent } from './components/case-studies/case-studies.component';
import { ContactComponent } from './components/contact/contact.component';
import { MainLayoutComponent } from './main-layout.component';

const routes: Routes = [
  {
    path: '',
    component: MainLayoutComponent,
    children: [
      { path: '', redirectTo: 'about', pathMatch: 'full' },
      { path: 'home', component: AboutComponent },
      { path: 'about', component: AboutComponent },
      { path: 'solutions', component: SolutionsComponent },
      { path: 'design-tool', component: DesignToolComponent },
      { path: 'case-studies', component: CaseStudiesComponent },
      { path: 'contact', component: ContactComponent },
      { path: 'services', component: ServicesComponent },
      { path: 'projects', component: ProjectsComponent },
      { path: 'brands', component: BrandsComponent },
      { path: 'clients', component: ClientsComponent }
    ]
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }