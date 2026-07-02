resource "aws_security_group" "fastapi_sg" {
  name        = "fastapi-sg"
  description = "Security group for FastAPI server"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_instance" "fastapi_server" {
  ami                    = "ami-0d52744d6551d851e"
  instance_type          = "t3.micro"
  key_name = "terraform-key"
  vpc_security_group_ids = [aws_security_group.fastapi_sg.id]

  tags = {
    Name = "terraform-fastapi-server"
  }
}
