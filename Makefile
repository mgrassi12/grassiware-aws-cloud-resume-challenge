.PHONY: build

build:
	sam build

deploy-infra:
	sam build && aws-vault exec mgrassi_admin --no-session -- sam deploy

deploy-site:
	aws-vault exec mgrassi_admin --no-session -- aws s3 sync ./resume-page s3://cloud-resume-challenge-grassiware-sam