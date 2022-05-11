FROM gitpod/workspace-full:latest

USER gitpod
# Install deps
ADD requirements.txt /home/gitpod/
ADD package-lock.json /home/gitpod/
ADD package.json /home/gitpod/
RUN pip install -r /home/gitpod/requirements.txt
RUN npm install --save-dev
RUN npm install -g truffle 
RUN npm install -g @graphprotocol/graph-cli

# Expose port
EXPOSE 8501

# # Start App
# CMD [ "tail", "-f" ,"/dev/null" ]