# Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

import logging
import boto3

logging.basicConfig()
logger = logging.getLogger()
logging.getLogger("botocore").setLevel(logging.ERROR)
logger.setLevel(logging.INFO)


def get_outputs_from_record(rec_id: str, client: boto3.client) -> dict:
    """Get output parameters from AWS Service Catalog Record Id

    Args:
        rec_id (str): Service Catalog Record Id
        client (boto3.client): Boto3 Client for Service Catalog

    Returns:
        dict: {'OutputKey1': 'OutputValue1'}
    """
    outputs = dict()
    logging.info(f"Getting Outputs for Record Id:{rec_id}")
    re = client.describe_record(
        Id=rec_id
    )
    for _op in re['RecordOutputs']:
        outputs[_op['OutputKey']] = _op['OutputValue']

    return outputs
