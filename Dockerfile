FROM gitpod/workspace-full

WORKDIR /home

# Install deps
ADD requirements.txt /home/
ADD package-lock.json /home/
ADD package.json /home/
RUN pip install -r requirements.txt
RUN npm install --save-dev
RUN npm install truffle -g

# Expose port
EXPOSE 8501

# Start App
CMD [ "tail", "-f" ,"/dev/null" ]