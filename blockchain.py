# -*- coding: utf-8 -*-
"""
Created on Tue Apr  8 21:43:39 2025

@author: Shahriar
"""
import datetime
import hashlib
import json
from flask import Flask, jsonify


class BlockChain:
    def __init__(self):
        self.chain = []
        self.createBlock(proof=1, prevHash='0')
        # genesis block creation, the first block of the chain

    def createBlock(self, proof, prevHash):
        block = {
        'index': len(self.chain) + 1,
        'timeStamp': str(datetime.datetime.now()),  # If using: from datetime import datetime, then just datetime.now()
        'proof': proof,
        'prevHash': prevHash,
    }
        self.chain.append(block)
        return block

    def get_previous_block(self):
        return self.chain[-1]

    def proof_of_work(self, prevProof):
        new_proof = 1
        check_proof=False
        
        while check_proof is False:
            hash_operation=hashlib.sha256(str(new_proof**2-prevProof**2).encode()).hexdigest()
            if hash_operation[:4]=='0000':
                check_proof=True
            else:
                new_proof+=1
        return new_proof
    
    def hash(self,block):
        encoded_block=json.dump(block,sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()
            
    
    def is_chain_valid(self,chain):
        previous_block=chain[0]
        block_index=1
        while block_index<len(chain):
            block=chain[block_index]
            if block['prevHash']!=self.hash(previous_block):
                return False
            previous_proof=previous_block['proof']
            proof=block['proof']
            hash_operation=hashlib.sha256(str(proof**2-previous_proof**2).encode()).hexdigest()
            if hash_operation[:4]!='0000':
                return False
            previous_block=block
            block_index+=1
        return True
            
app=Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False
blockChain=BlockChain()        

@app.route("/mine_block",methods=['GET'])
def mine_block():
    previous_block=blockChain.get_previous_block()
    previous_proof=previous_block['proof']
    proof=blockChain.proof_of_work(previous_proof)
    previous_hash=blockChain.hash(previous_block)
    block=blockChain.createBlock(proof, previous_hash)
    response={'message':'Mined a block',
              'index':block['index'],
              'timestamp':block['timeStamp'],
              'proof':block['proof'],
              'prevHash':block['prevHash']}
    return jsonify(response),200

@app.route("/get_blocks",methods=['GET'])
def get_chains():
    response={
        'chain':blockChain.chain,
        'length':len(blockChain.chain)
        }
    return jsonify(response),200

@app.route("verify_chain",methods=['GET'])
def is_chain_valid():
    is_valid=blockChain.is_chain_valid(blockChain.chain)
    if is_valid:
        response={'message':'Block is valid'}
    else:
        response={'message':'Block is not valid'}
        
    return jsonify(response, 200)

app.run(host='0.0.0.0',port=5000)
            
            