-- Insert users
INSERT INTO public.users (display_name, handle, cognito_user_id)
VALUES
    ('Andrew Brown', 'andrewbrown', 'MOCK'),
    ('Andrew Bayko', 'bayko', 'MOCK');

-- Insert activity for Andrew Brown
INSERT INTO public.activities (user_uuid, message, expires_at)
SELECT uuid, 'This was imported as seed data!', current_timestamp + interval '10 day'
FROM public.users
WHERE handle = 'andrewbrown';