FROM ubuntu:22.04

RUN apt update && apt upgrade -y && apt install sudo zsh git vim zip wget curl python3-pip sqlite3 bpytop -y

# Powerlevel10k
RUN mkdir /usr/share/fonts/truetype/meslo
RUN wget https://github.com/romkatv/powerlevel10k-media/raw/master/MesloLGS%20NF%20Regular.ttf \
    -O /usr/share/fonts/truetype/meslo/MesloLGSNFRegular.ttf
RUN wget https://github.com/romkatv/powerlevel10k-media/raw/master/MesloLGS%20NF%20Bold.ttf \
    -O /usr/share/fonts/truetype/meslo/MesloLGSNF20Bold.ttf
RUN wget https://github.com/romkatv/powerlevel10k-media/raw/master/MesloLGS%20NF%20Italic.ttf \
    -O /usr/share/fonts/truetype/meslo/MesloLGSNFItalic.ttf
RUN wget https://github.com/romkatv/powerlevel10k-media/raw/master/MesloLGS%20NF%20Bold%20Italic.ttf \
    -O /usr/share/fonts/truetype/meslo/MesloLGSNFBoldItalic.ttf

# User
RUN adduser --shell /usr/bin/zsh --gecos '' --ingroup sudo --disabled-password shorten
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers
USER shorten

# Zsh
RUN sh -c "$(wget https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh -O -)"
RUN git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k

COPY .zshrc /home/shorten
COPY .p10k.zsh /home/shorten