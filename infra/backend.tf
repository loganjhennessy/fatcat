terraform {
  backend "gcs" {
    bucket  = "rent_right_terraform_state"
    prefix  = "prod"
  }
}