from dataclasses import dataclass, asdict


@dataclass
class PersonSchema:
    full_name: str
    industry: str
    job_title: str
    sub_role: str
    industry_2: str
    emails: str
    mobile: str
    phone_numbers: str
    company_name: str
    company_industry: str
    company_website: str
    company_size: str
    company_founded: str
    location: str
    locality: str
    metro: str
    region: str
    skills: str
    first_name: str
    middle_initial: str
    middle_name: str
    last_name: str
    birth_year: str
    birth_date: str
    gender: str
    linkedin_url: str
    linkedin_username: str
    facebook_url: str
    facebook_username: str
    twitter_url: str
    twitter_username: str
    github_url: str
    github_username: str
    company_linkedin_url: str
    company_facebook_url: str
    company_twitter_url: str
    company_location_name: str
    company_location_locality: str
    company_location_metro: str
    company_location_region: str
    company_location_geo: str
    company_location_street_address: str
    company_location_address_line_2: str
    company_location_postal_code: str
    company_location_country: str
    company_location_continent: str
    last_updated: str
    start_date: str
    job_summary: str
    location_country: str
    location_continent: str
    street_address: str
    address_line_2: str
    postal_code: str
    location_geo: str
    last_updated: str
    linkedin_connections: str
    inferred_salary: str
    years_experience: str
    summary: str
    countries: str
    interests: str

    def as_dict(self):
        return asdict(self)