CREATE OR REPLACE FUNCTION pair.app_doc_summary_version(p_app_num CHARACTER VARYING)
RETURNS JSON LANGUAGE plpgsql STABLE AS $$
DECLARE final_data JSON;
BEGIN
    SELECT jsonb_agg(to_jsonb(t)) INTO final_data
    FROM (
        SELECT
            ad.app_num,
            ifw.doc_desc,
            ifw.mail_room_date
        FROM core.pats ad
        JOIN data_tools.patents_demo ifw ON ad.id = ifw.app_data_id
       JOIN core.app_data ap ON ap.id = ifw.app_data_id
        WHERE ad.app_num = p_app_num
    ) t;
    RETURN final_data;
END;
$$;
