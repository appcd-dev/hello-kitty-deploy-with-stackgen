
output "aws_s3_hello_kitty_assets_bucket_name" {
  value = module.appcd_c5f14030-2682-57e2-b121-e813125256b2.bucket_name
  sensitive = false
}


output "aws_s3_hello_kitty_assets_arn" {
  value = module.appcd_c5f14030-2682-57e2-b121-e813125256b2.arn
  sensitive = false
}


output "aws_s3_hello_kitty_assets_kms_arn" {
  value = module.appcd_c5f14030-2682-57e2-b121-e813125256b2.kms_arn
  sensitive = false
}


output "aws_s3_hello_kitty_assets_bucket_website_endpoint" {
  value = module.appcd_c5f14030-2682-57e2-b121-e813125256b2.bucket_website_endpoint
  sensitive = false
}


output "aws_cloudwatch_log_group_aws_lambda_hello_kitty_with_stackgen_function_arn" {
  value = module.appcd_fac04857-dd47-5515-84ab-7db8952961fd.arn
  sensitive = false
}


output "aws_cloudwatch_log_group_aws_lambda_hello_kitty_with_stackgen_function_name" {
  value = module.appcd_fac04857-dd47-5515-84ab-7db8952961fd.name
  sensitive = false
}


output "aws_lambda_hello_kitty_with_stackgen_function_function_url" {
  value = module.appcd_a7b0dbf8-ab3f-5861-8d42-42ee6425c3e6.function_url
  sensitive = false
}


output "aws_lambda_hello_kitty_with_stackgen_function_function_name" {
  value = module.appcd_a7b0dbf8-ab3f-5861-8d42-42ee6425c3e6.function_name
  sensitive = false
}


output "aws_lambda_hello_kitty_with_stackgen_function_invoke_arn" {
  value = module.appcd_a7b0dbf8-ab3f-5861-8d42-42ee6425c3e6.invoke_arn
  sensitive = false
}


output "aws_lambda_hello_kitty_with_stackgen_function_function_arn" {
  value = module.appcd_a7b0dbf8-ab3f-5861-8d42-42ee6425c3e6.function_arn
  sensitive = false
}


output "aws_iam_role_hello_kitty_with_stackgen_role_name" {
  value = module.appcd_556e36fe-496a-5f72-9460-247c86932a93.name
  sensitive = false
}


output "aws_iam_role_hello_kitty_with_stackgen_role_arn" {
  value = module.appcd_556e36fe-496a-5f72-9460-247c86932a93.arn
  sensitive = false
}
